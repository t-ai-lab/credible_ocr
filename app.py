from flask import Flask, request, send_from_directory
import pandas as pd
import camelot
from flask_cors import CORS
import warnings

def read_and_to_excel(pdf_file):
    tables = camelot.read_pdf(pdf_file,flavor='stream',pages='all', split_text=False, edge_tol=500, encoding = "utf-8")
    df_cam = pd.DataFrame()
    for i in range(len(tables)):
        df_cam = df_cam.append(tables[i].df, ignore_index=True)

    name_of_file = pdf_file[:-4]+".json"
    df_cam.to_json(name_of_file)

    return name_of_file



warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)


@app.route('/pdf_reader', methods=['POST'])
def pdf_reader():
    file1 = "None"

    # Giving an ID (Counter) to each user
    f = open("counter.txt", "r")
    counter = f.read()
    f.close()

    

    name1 = counter + "_1.pdf"
    

    # Writing new counter
    f = open("counter.txt", "w")
    f.write(str(int(counter) + 1))
    f.close()

    # Get the file data from the request
    try:
        file1 = request.files['file']
    except Exception as ex:
        print(ex.__str__())
        

    # saving the files
    try:
        file1.save(name1)
    except Exception as ex:
        print(ex.__str__())
        
   
    #try:
    path_of_file = read_and_to_excel(name1)
    #except Exception as ex:
    #    print(repr(ex))
    #    pass
    

    return send_from_directory(directory = "",path = path_of_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

