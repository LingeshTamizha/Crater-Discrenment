from io import BytesIO
from sqlalchemy import func
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from flask import make_response


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        upload = Upload(filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()
        return f'Uploaded: {file.filename}'
    return render_template('index.html')

@app.route('/download/<upload_id>')
def download(upload_id):
    upload = Upload.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data), download_name=upload.filename, as_attachment=True)

@app.route('/report')
def report():
    filenames_with_counts = db.session.query(Upload.filename, func.count(Upload.id)).group_by(Upload.filename).all()
    sorted_filenames_with_counts = sorted(filenames_with_counts, key=lambda x: x[1], reverse=True)
    return render_template('report.html', filenames_with_counts=sorted_filenames_with_counts)



if __name__ == '_main_':
    app.run()