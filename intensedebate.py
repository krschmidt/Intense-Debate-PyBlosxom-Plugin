"""
intensedebate.py pyblosxom plugin
Lets you use IntenseDebate with pyblosxom

IntenseDebate (www.intensedebate.com) is a comment service
which provides advanced utilities for managing comments including
threading, approval, spam checking, and more.

To use:
Add the variable intense_debate_id to your config.py file, where your id
is the long string after idcomments_acct in the javascript IntenseDebate
gives you. Then simply put the variable $intenseDebate where you want 
your comments to appear.

You can also use the variable $commentCount to get a count of the number of
comments in the story, but this variable will only be populated if we're
looking at a single story. Finding the number of comments for each story
while looking at a collection of stories is beyond my current understanding of
PyBlosxom.

Thank you Jordan Sissel (http://www.semicomplete.com) for your page
title plugin, which I used to develop this plugin.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301, USA.

"""

__author__ = 'Kyle Schmidt <krschmidt@gmail.com>'
__version__ = '1'
__url__ = 'http://www.kyleschmidt.com'

def verify_installation(request):
    config = request.getConfiguration()
    if not config.has_key('intense_debate_id'):
        print "missing intense_Debate_ID variable"
        return 0
    return 1

def cb_prepare(args):
  request = args["request"]
  config = request.getConfiguration()
  data = request.getData()
  if data.has_key("entry_list"):
    if len(data["entry_list"]) == 1:
        data["intenseDebate"] = "<script>var idcomments_acct = \'" + config['intense_debate_id'] + "\'; var idcomments_post_id; var idcomments_post_url; </script> <span id=\"IDCommentsPostTitle\" style=\"display:none\"></span> <script type=\'text/javascript\' src=\'http://www.intensedebate.com/js/genericCommentWrapperV2.js\'></script>"
        data["commentCount"] = "<script>var idcomments_acct = \'" + config['intense_debate_id'] + "\';var idcomments_post_id; var idcomments_post_url;</script> <script type=\"text/javascript\" src=\"http://www.intensedebate.com/js/genericLinkWrapperV2.js\"></script>"
    elif len(data["entry_list"]) > 1:
        data["intenseDebate"] = ""
       
