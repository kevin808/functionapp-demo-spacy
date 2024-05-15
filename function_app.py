import azure.functions as func
import datetime
import json
import logging
import spacy

app = func.FunctionApp()

@app.route(route="Hello", auth_level=func.AuthLevel.ANONYMOUS)
def Hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        #nerModel = spacy.load('./NER_model')
        nerModel = spacy.load("en_core_web_sm") 
    except:
        nerModel = None
    if nerModel==None:
        #final_output = json.dumps(jsonOutput.__dict__)
        #return func.HttpResponse(final_output, mimetype="application/json") 
        logging.info("Model could not load properly")
        return func.HttpResponse("Model could not load properly")
    else:
        logging.info("Model loaded properly")
        doc = nerModel("data")  
        entities = {ent.label_: ent.text for ent in doc.ents}
        return func.HttpResponse(f"Named Entities: {entities}") 
