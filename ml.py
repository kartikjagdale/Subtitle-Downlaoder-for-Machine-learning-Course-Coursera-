#Download all subtitle of videos on coursera for Machine Learning Course by Andrew Ng
#Author: Hebi
#Note: Before sunning the script create a Folder Named: 'subtitle' in the same directory

import urllib2
url = 'https://class.coursera.org/ml-005/lecture/subtitles?q='
url2 = '_en&format=srt'

print "Downloaded Subtitle No. ", 
for i in range(1,115):
    try:
        page = urllib2.urlopen(url+str(i)+url2).read();
        f =  open('subtitle\lec_'+str(i)+'.srt','w+');
        f.write(page);
        f.close();
        print i,;
    except (urllib2.HTTPError, urllib2.URLError) as e:
        print '\nProblem Downloading file: ',i
        print 'OR Connection Error'

print '\nDownload Finished\nHappy Coding!!!'
