from  flask import Flask , render_template
app= Flask(__name__)

@app.route('/')
def myfun():
     return render_template('s.html')

if __name__ == "__main__":
    app.run()
# import psycopg2

# conncetion=psycopg2.connect(
#     host="localhost",
#     user="postgres",
#     password="admin",
#     dbname="postgres"
# )
#mycursor= conncetion.cursor()
# # mycursor.execute("select * from nani1")
# val = [(7200,'puri',11267),(820,'jony',1009)]
# mycursor.executemany("INSERT INTO Student1 (id,name,salary) VALUES (%s,%s, %s)",val)
# conncetion.commit()
# print(mycursor.rowcount, "record inserted.")
# mycursor.execute("select * from Student1")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
# mycursor.close()
#  conncetion.close()
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <h1>submit the application</h1>
#     <form id="myform">
#         <label>phone:</label>
#         <input type="text" id="phone" name="phone" required><br>
#         <label>password:</label>
#         <input type="text" id="password" name="password" required><br>
#         <button type="submit">submit</button>
#     </form>
#     <script>
#         document.getElementById('myform').addEventListener('submit',function(event){
# event.preventDefault();
# const phone= document.getElementById('phone').value;
# const password = document.getElementById('password').value;
# const data = {
#     phone: phone,
#     password:password
# }

# fetch('http://localhost:5000/postitem',{
# method:'POST',
# headers:{
#     'Content-Type':'application/json'
# },
# body:JSON.stringify(data)
# })
# .then(Response=>Response.json())
# .then(data=>{
#     console.log('success:',data);
#     alert("data inserted successfully")

# })
# .catch((error)=>{
#     console.log('error',error);
#     alert('data insertion failed')
# })

#         })
#     </script>
# </body>
# </html>
#