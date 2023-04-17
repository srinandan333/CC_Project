from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

def add(n1, n2):
    URL = 'http://addition-service:'
    port = 5051
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def minus(n1, n2):
    URL = 'http://subtraction-service:'
    port = 5052
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def multiply(n1, n2):
    URL = 'http://multiplication-service:'
    port = 5053
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def divide(n1, n2):
    URL = 'http://division-service:'
    port = 5054
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def gcd(n1, n2):
    URL = 'http://gcd-service:'
    port = 5055
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def lcm(n1, n2):
    URL = 'http://lcm-service:'
    port = 5056
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def modulus(n1, n2):
    URL = 'http://modulus-service:'
    port = 5057
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']
   
def exponent(n1, n2):
    URL = 'http://exponent-service:'
    port = 5058
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']
        
def greater_than(n1, n2):
    URL = 'http://greater_than-service:'
    port = 5059
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def less_than(n1, n2):
    URL = 'http://less_than-service:'
    port = 5060
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

def equal(n1, n2):
    URL = 'http://equal-service:'
    port = 5061
    comb = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    ans = requests.get(comb)
    print(ans)
    return ans.json()['res']

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        a = int(request.form.get('first'))
        b = int(request.form.get('second'))
        op = request.form.get('op')
        res = 0

        if op == 'add':
            res = add(a, b)

        elif op == 'minus':
            res = minus(a, b)

        elif op == 'multiply':
            res = multiply(a, b)

        elif op == 'divide':
            if b==0:
                        res = 'Zero Division Error'
            else:
                        res = divide(a, b) 

        elif op == 'gcd':
            res = gcd(a, b)

        elif op == 'lcm':
            res = lcm(a, b) 

        elif op == 'modulus':
            if b==0:
                        res = 'Zero Division Error'
            else:
                        res = modulus(a, b)                                

        elif op == 'exponent':
            res = exponent(a, b) 

        elif op == 'greater_than':
            res = greater_than(a, b)

        elif op == 'less_than':
            res = less_than(a, b)

        elif op == 'equal':
            res = equal(a, b)
               
        flash(f'The res of operation {op} on {a} and {b} is {res}')
        return render_template('index.html')
    
    except:
        flash(f'No input value')
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")