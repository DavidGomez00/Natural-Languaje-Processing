"""
Code adapted from the NLP class by Daniel Jurafski & Christopher Manning

Group: David David Esme: David Andrés, David Gómez y Esmeralda Madrazo

This code was made in colaboration with Group Juan Victor: Victor Viñas and Juan Becerro
"""
import sys
import os
import re
import pprint

emails = '((?:\w[.-]?)+)\s?(?:@| WHERE | at |&#x40;)\s?-?((?:\w(?:\sdot\s|[;.-])?)+)-?(?:.|\sDOM\s|\sdot\s|;)-?[Ee]-?[Dd]-?[Uu]'
phone_pat = '(?:\(|[ ]|^)((?:[2-9])(?:[02-9]{2}|[02-9]1|1[02-9]))\)?-? ?([0-9]{3})-? ?([0-9]{4})[^0-9]'

""" 
This function takes in a filename along with the file object and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers
"""
def process_file(name, f):
    res = []
    for line in f:
        matches = re.findall(emails,line)
        for m in matches:
            email = '%s@%s.edu' % m
            email = email.replace('-', '')
            email = email.replace('WHERE', '@')
            email = email.replace('DOM', '.')
            email = email.replace(' dot ', '.')
            email = email.replace(' dt ', '.')
            email = email.replace(';', '.')
            email = email.replace(' at ', '@')
            email = email.replace('&#x40;', '@')
            email = email.replace(' ', '.')
            print(f'{email}')
            res.append((name,'e',email))

        p_matches = re.findall(phone_pat, line)
        for m in p_matches:
            phone = '%s-%s-%s' % m
            res.append((name, 'p', phone))        
        
    return res

"""
You should not need to edit this function.
Given a path to a directory, it processes all files
in that directory using the method 'process_file',
and collects all results in a unique list of tuples 
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        path = os.path.join(data_path,fname)
        f = open(path,'r',encoding="utf-8",errors = "ignore")
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))



"""
The main program takes a directory name and gold file (you should not need to edit it).
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    guess_list = process_dir('./Assignment1/data/dev')
    gold_list =  get_gold('./Assignment1/data/devGOLD')
    score(guess_list, gold_list)
