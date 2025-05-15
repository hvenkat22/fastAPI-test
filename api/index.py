from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Sample data (your full JSON goes here)
data = [{"name":"KMdM","marks":97},{"name":"Ljxb8yGG","marks":53},{"name":"Ktc","marks":2},{"name":"2EQdig","marks":24},{"name":"bHBAz5","marks":11},{"name":"HrVGb7PSd9","marks":5},{"name":"bobP6","marks":16},{"name":"qS6GOp","marks":45},{"name":"IINJL","marks":43},{"name":"sfSroo","marks":17},{"name":"kYcSWpe","marks":36},{"name":"STDaGPmAw","marks":8},{"name":"QigPIIvXa","marks":47},{"name":"Xio0peB","marks":42},{"name":"pRd","marks":22},{"name":"awxZV","marks":64},{"name":"8g","marks":10},{"name":"xR","marks":17},{"name":"WOK54KDSI","marks":89},{"name":"EFp5","marks":61},{"name":"Hlo0Y","marks":76},{"name":"nLgNgwR","marks":36},{"name":"y","marks":94},{"name":"WC05aA","marks":58},{"name":"hMHGWXK","marks":32},{"name":"g","marks":3},{"name":"Nj0oHEadom","marks":96},{"name":"Yl7k7DA61A","marks":73},{"name":"Q9PjIVWxP","marks":6},{"name":"hZQi","marks":76},{"name":"L","marks":28},{"name":"wb","marks":91},{"name":"x","marks":77},{"name":"vB","marks":53},{"name":"Z3x2oHJi","marks":83},{"name":"TX4","marks":23},{"name":"Vc","marks":15},{"name":"QODq","marks":63},{"name":"cg","marks":4},{"name":"KBkv9","marks":38},{"name":"hL8hbe","marks":55},{"name":"vJ","marks":68},{"name":"e4Gz","marks":60},{"name":"tTmAUqgM","marks":68},{"name":"alJ8L2Qyy","marks":24},{"name":"akFiSEoN","marks":80},{"name":"T0fiY","marks":73},{"name":"r3lfSVq","marks":55},{"name":"cf","marks":78},{"name":"dfVWjkOWHi","marks":14},{"name":"1Jw12vF","marks":34},{"name":"6b67F","marks":71},{"name":"cxKd3","marks":46},{"name":"kdxlHQIf1D","marks":9},{"name":"bIR","marks":26},{"name":"tKnGT8","marks":32},{"name":"IgsXYly","marks":8},{"name":"oIOiyU6j","marks":35},{"name":"MaF1FHKdO5","marks":57},{"name":"m7Om1u","marks":57},{"name":"9V5gK","marks":88},{"name":"Dq8Pi","marks":90},{"name":"JHpK6PDsv","marks":73},{"name":"50NjOBJlQ","marks":6},{"name":"Sjr","marks":35},{"name":"4gxakUO","marks":10},{"name":"Tf","marks":24},{"name":"lmTwWcXt","marks":79},{"name":"oMJjv","marks":77},{"name":"JMoTIGt","marks":73},{"name":"B","marks":41},{"name":"6q","marks":17},{"name":"fJkcCzp","marks":72},{"name":"0lP2BY5nGk","marks":46},{"name":"68JDlL0Lfa","marks":45},{"name":"gK","marks":23},{"name":"TzxfHVvDX","marks":20},{"name":"A2u6ta8Rc","marks":63},{"name":"QzIk","marks":94},{"name":"k","marks":83},{"name":"Mmos","marks":53},{"name":"zFNR","marks":47},{"name":"K5n8VAFNy","marks":18},{"name":"yJsxY","marks":34},{"name":"5xYh19","marks":17},{"name":"b","marks":19},{"name":"ydwJcExhV6","marks":45},{"name":"yG","marks":3},{"name":"cYq","marks":26},{"name":"k4LVYh","marks":47},{"name":"yS29mpMRbV","marks":13},{"name":"xt8","marks":42},{"name":"3zy6ZZy5U","marks":6},{"name":"OcyAKDGM","marks":69},{"name":"JIQ9","marks":76},{"name":"VqajMqXWnR","marks":99},{"name":"KlCqqLyd","marks":99},{"name":"rB","marks":48},{"name":"69yT4","marks":41},{"name":"HItmg","marks":35}]

# Preprocess into a dictionary for fast lookup
marks_dict = {item["name"]: item["marks"] for item in data}

@app.get("/")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    results = [marks_dict.get(name, None) for name in names]
    return JSONResponse(content={"marks": results})
