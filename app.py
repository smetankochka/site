from flask import Flask, render_template
import json

app = Flask(__name__)

# Загружаем данные из JSON файла
with open("blog_posts.json", "r") as f:
    blog_posts = json.load(f)

# Биография
bio = [
    " Hi! I'm Maksim, a 17 y.o. dev from Vladivostok",
    "I'm currently studying at University School of the Far Eastern Federal University, previously studied at SESC NSU (yeah, my mistake)",
    "I'm currently working on programming competitions, golang language and computer vision.",
    "I've got a blog (Пустой пока пох). I also sometimes write some about my life in my Telegram channel (in Russian).",
]

@app.route("/")
def index():
    return render_template("index.html", bio=bio, github_link="https://github.com/smetankochka", telegram_link="https://t.me/smetankasixtyfive", telegram_ch_link="https://t.me/smetankochka")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=blog_posts, enumerate=enumerate)

@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    post = blog_posts[post_id]
    return render_template("blog_post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
