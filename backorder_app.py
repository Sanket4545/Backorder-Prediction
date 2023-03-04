import joblib
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=["POST"])
def brain():
    national_inv=float(request.form['national_inv'])
    lead_time=float(request.form['lead_time'])
    sales_1_month=float(request.form['sales_1_month'])
    pieces_past_due=float(request.form['pieces_past_due'])
    perf_6_month_avg=float(request.form['perf_6_month_avg'])
    in_transit_qty=float(request.form['in_transit_qty'])
    local_bo_qty=float(request.form['local_bo_qty'])
    deck_risk=float(request.form['deck_risk'])
    oe_constraint=float(request.form['oe_constraint'])
    ppap_risk=float(request.form['ppap_risk'])
    stop_auto_buy=float(request.form['stop_auto_buy'])
    rev_stop=float(request.form['rev_stop'])
     
    values=[national_inv,lead_time,sales_1_month,pieces_past_due,perf_6_month_avg,in_transit_qty,local_bo_qty,deck_risk,oe_constraint,ppap_risk,stop_auto_buy,rev_stop]
    

    joblib.load('backorder_model','r')
    model = joblib.load(open('backorder_model','rb'))
    arr = [values]
    acc = model.predict(arr)
    # print(acc)

    for i in acc:
        if i ==0:
            return "Product went on Backorder"
        else:
            return "Did not go on backorder"
        break


if __name__ == '__main__':
    app.run(debug=True)
