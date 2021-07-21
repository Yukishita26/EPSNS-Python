import requests
import datetime
url = "https://versatileapi.herokuapp.com/api"
def toJST(s):
    return (datetime.datetime.strptime(s[:-6], "%Y-%m-%dT%H:%M:%S.%f") + datetime.timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S")

class EngineerSNS(object):
    """
    read and write SNS only for engineers and programmers

    """
    def __init__(self):
        self.userdict = {}
        self.blockedusers = set()
        self.posts = None
        self.users = None
    def register_user(self, name, description=""):
        """
        make new user

        Parameters
        ----------
        name: str
            your screen name
        description: str, default ""
            your description

        Returns
        -------
        requests.models.Response
            response status code
        """
        return requests.post(url + "/user/create_user",
              json = {
                  "name": name,
                  "description": description
              })
    def update_user(self, name, description=""):
        """
        update your user description

        Parameters
        ----------
        name: str
            your screen name
        description: str, default ""
            your description

        Returns
        -------
        requests.models.Response
            response status code
        """
        return requests.put(url + "/user/create_user",
              json = {
                  "name": name,
                  "description": description
              })    
    def get_all_users(self, only_get=False):
        """
        get all user list, print names and descriptions to std output, and save dictionary from ID to screen name 

        Parameters
        ----------
        only_get: bool, default False
            suppress output
        
        Returns
        -------
        requests.models.Response
            response status code
        """
        users_r = requests.get(url + "/user/all")
        for user in users_r.json():
            print(user["name"], user["description"])
        self.userdict = {user["id"]:user["name"] for user in users_r.json()}
        self.users = users_r.json()
        return users_r

    def get_latest_posts(self, limit=20, only_get=False, show_id=False):
        """
        get the last some posts and print post dates, names, and texts

        Parameters
        ----------
        limit: int, default 20
            number of posts to retrieve
        only_get: bool, default False
            suppress output
        show_id: bool, default False
            True if showing user ID instead of screen name 

        Returns
        -------
        requests.models.Response
            response status code
        """
        posts_r = requests.get(url + "/text/all?$orderby=_created_at desc&$limit={}".format(limit))
        print(posts_r)
        for post in posts_r.json():
            if post["_user_id"] not in self.blockedusers:
                if show_id:
                    print(toJST(post["_created_at"]), post["_user_id"], post["text"])
                else:
                    print(toJST(post["_created_at"]), self.userdict.get(post["_user_id"], "unknown"), post["text"])
        self.posts = posts_r.json()
        return posts_r
    
    def show_again_latest_posts(self, show_id=False):
        """
        show the posts that got last and print post dates, names, and texts

        Parameters
        ----------
        show_id: bool, default False
            True if showing user ID instead of screen name 

        Returns
        -------
        None
        """
        for post in self.posts:
            if post["_user_id"] not in self.blockedusers:
                if show_id:
                    print(toJST(post["_created_at"]), post["_user_id"], post["text"])
                else:
                    print(toJST(post["_created_at"]), self.userdict.get(post["_user_id"], "unknown"), post["text"])
    
    def post_new_text(self, text):
        """
        post a sentence

        Parameters
        ----------
        text: str
            text to post

        Returns
        -------
        requests.models.Response
            response status code
        """
        return requests.post(url + "/text",
              headers = {'Authorization': 'HelloWorld'},
              json = {
                  "text": text
              })
    
    def block_user(self, userid):
        """
        add a user to block list

        Parameters
        ----------
        userid: str
            user ID to block

        Returns
        -------
        None
        """
        self.blockedusers.add(userid)
        
if __name__=="__main__":
    print("test")
    sns = EngineerSNS()
    sns.get_all_users()
    sns.get_latest_posts()
