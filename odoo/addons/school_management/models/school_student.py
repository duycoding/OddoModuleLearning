from odoo import models, fields, api
from pyspark.sql import SparkSession

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    grade = fields.Char(string='Grade')

    @api.model
    def process_student_data_with_spark(self):
        # Khởi tạo SparkSession
        spark = SparkSession.builder \
            .appName("OdooIntegration") \
            .getOrCreate()

        # Lấy dữ liệu từ Odoo và chuyển đổi sang định dạng phù hợp cho Spark
        students = self.search([])
        data = [(student.name, student.age, student.grade) for student in students]
        columns = ["Name", "Age", "Grade"]

        # Tạo DataFrame từ dữ liệu
        df = spark.createDataFrame(data, columns)

        # Thực hiện các thao tác trên DataFrame
        df.show()

        # Ví dụ: tính tuổi trung bình của các học sinh
        avg_age = df.groupBy().avg('Age').collect()[0][0]
        result_str = f"Average Age: {avg_age}"

        # Tạo một bản ghi mới trong Odoo để lưu kết quả
        self.env['school.student.result'].create({
            'name': 'Spark Processed Data',
            'result': result_str
        })

        # Dừng SparkSession
        spark.stop()

class SchoolStudentResult(models.Model):
    _name = 'school.student.result'
    _description = 'School Student Result'

    name = fields.Char(string='Name')
    result = fields.Text(string='Result')
