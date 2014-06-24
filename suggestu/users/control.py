# handle user search history
from users.models import User
from django.utils import timezone

def add_to_history(query, username):
    #print query, " | ", username
    try:
        s_history = User.objects.get(user_id__contains=username)
        #print "User %s found in DB!\n" % (username)
    except:
        s_history = User( user_id=username, last_search=timezone.now())    
        print "User %s not found in DB. Created one." % (username)
    '''
    # split multi-word query into individual ones'
    for word in query.split():
        if word not in s_history.keywords:
            s_history.keywords.append(word)
    '''
    # append query without splitting multi-word query
    if query not in s_history.keywords:
        s_history.keywords.append(query)
    else:
        s_history.keywords.remove(query)
        s_history.keywords.append(query)
    s_history.save()
    #print "History For username: %s \nKeywords: %s" \
    #    % (username, str(s_history.keywords))
    return s_history.keywords
