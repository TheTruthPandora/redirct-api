from flask import Flask, redirect, request, jsonify

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirect_api():
    target_url = request.args.get('href')
    if target_url:
        return redirect(target_url)
    else:
        return jsonify({'error': 'No URL provided.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)