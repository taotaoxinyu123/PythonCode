"""
本文学习使用flask的使用：
    1)flask库比较灵活，没有像java的spring那样把很多给你做好了，它实现某些功能是需要在flask上进行扩展的
        默认情况下，Flask 不包含数据库抽象层、表单验证，或是其它任何已有多种库可以胜任的功能
        然而，Flask 支持用扩展来给应用添加这些功能，如同是 Flask 本身实现的一样
        众多的扩展提供了数据库集成、表单验证、上传处理、各种各样的开放认证技术等功能。Flask 也许是“微小”的，但它已准备好在需求繁杂的生产环境中投入使用
    2)由于python3 与python2在Unicode 的变化,造成了flask库对于某些模块不能很好的支持python3，所以flask建议使用python2.7
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    print("this is hello function")
    return "Hello, World!"
@app.route('/test/')
def test():
    print("this is test function")
    return "test!"
app.run(host='127.0.0.1',port='8081') #必须卸载后面 不然访问404；或者写在主模块里面