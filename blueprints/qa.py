from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import QuestionForm, CommentForm
from models import QuestionModel, CommentModel
from exts import db
from decorators import login_required

bp = Blueprint('qa', __name__, url_prefix="/")


@bp.route("/")
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html", questions=questions)


@bp.route("/qa/public", methods=['GET', 'POST'])
@login_required
def public_question():
    if request.method == "GET":
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.title.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("qa.public_question"))


@bp.route("qa/detail/<qa_id>")
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html", question=question)


# @bp.route("/comment/public", methods=['POST'])
@bp.post("comment/public")
@login_required
def public_comment():
    form = CommentForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        comment = CommentModel(content=content, question_id=question_id, author_id=g.user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("qa.qa_detail", qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for("qa.qa_detail", qa_id=request.form.get("question_id")))


@bp.route("/search")
def search():
    # /search?q=flask
    # /search/<q>
    # post, request.form
    q = request.args.get("q")
    # 把所有包含q关键字的返回
    questions = QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template("index.html", questions=questions)


# 学习总结
# 1. url传参
# 2. 邮件发送
# 3. ajax
# 4. ORM与数据库
# 5. Jinja2模板
# 6. cookie与session原理
