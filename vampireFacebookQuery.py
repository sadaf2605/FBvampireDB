#for sending get request to facebook we will need this library

import urllib2



app_id = '498850750203566';
app_secret = '0f82df0f23260244cbbed2d5d54e484c';
my_url = 'localhost:8080';

code = s

# auth user
if code:
    dialog_url = 'https://www.facebook.com/dialog/oauth?client_id='+app_id + '&redirect_uri=' + my_url
    
    print"<script>top.location.href='" +dialog_url + "'</script>"

# get user access_token

token_url="https://graph.facebook.com/oauth/access_token?client_id="+app_id + "&client_secret=" +app_secret+ "&redirect_uri=" +my_url
print urllib2.urlopen(token).read()   
          #+ '&code=' + code
print token_url
access_token=token_url[13:]

fql_query_url = 'https://graph.facebook.com/'\
          + 'fql?q=SELECT+uid2+FROM+friend+WHERE+uid1=659142048'\
          + '&access_token=' +access_token

print fql_query_url
print urllib2.urlopen(fql_query_url).read()          
