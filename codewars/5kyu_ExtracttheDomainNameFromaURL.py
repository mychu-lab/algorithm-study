'''https://www.codewars.com/kata/514a024011ea4fb54200004b'''
def domain_name(url):
    return (url.replace('https://','').replace('http://','').replace('www.','').split('/')[0]).split('.')[0]