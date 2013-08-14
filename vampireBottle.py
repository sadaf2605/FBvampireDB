from bottle import route,get, run, request, template
import urllib2
import facebook
import requests

app_id = '498850750203566';
app_secret = '0f82df0f23260244cbbed2d5d54e484c';
my_url = 'http://localhost:8080/';

@get('/')
def welcomePage():
    verification_code=""
    if "code" in request.query:
        verification_code = request.query["code"]
    else:
        verification_code
    print verification_code
    if not verification_code:
        dialog_url = ( "http://www.facebook.com/dialog/oauth?" +
                           "client_id=" + app_id +
                           "&redirect_uri=" + my_url +
                           "&scope=publish_stream" )
        return "<script>top.location.href='" + dialog_url + "'</script>"
    else:
        token_url = ( "https://graph.facebook.com/oauth/access_token?" +
                          "client_id=" + app_id +
                          "&redirect_uri=" +my_url +
                          "&client_secret=" + app_secret +
                          "&code=" + verification_code )
        response = requests.get(token_url).content
        
        params = {}
        result = response.split("&", 1)
        for p in result:
            (k,v) = p.split("=")
            params[k] = v

        access_token = params['access_token']

        fql_query_url = 'https://graph.facebook.com/'\
          + 'fql?q=SELECT geometry FROM place WHERE page_id in(SELECT place_id FROM status WHERE uid = me() and place_id LIMIT 1)'\
          + '&access_token=' +access_token
        
    return "Welcome to FBvampireDB"+str(requests.get(fql_query_url).content)
@route('/my_ip')
def show_ip():
    ip = request.environ.get('REMOTE_ADDR')
    # or ip = request.get('REMOTE_ADDR')
    # or ip = request['REMOTE_ADDR']
    return template("oauth.html")
run(host='localhost', port=8080, debug=True)
