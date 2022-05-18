% Relleno el lexicon
lex(el, detms).
lex(un, detms).
lex(una, detfs).
lex(la, detfm).
lex(los, detmp).
lex(unos, detmp).
lex(unas, detfp).
lex(las, detfp).

lex(perro, nms).
lex(hueso, nms).
lex(estudiante, nms).

lex(perra, nfs).
lex(estudiante, nfs).

lex(perros, nmp).
lex(huesos, nmp).
lex(estudiantes, nmp).

lex(perras, nfp).
lex(estudiantes, nfp).

lex(bonita, adfs).
lex(bonitas, adfp).
lex(bonito, adms).
lex(bonitos, admp).

lex(ladra, vps).
lex(ladran, vpp).

lex(muerde, vts).
lex(muerden, vtp).

% Reglas del DCG
s --> nps, vps;
    npp, vpp.

nps --> detfs, nfs;
	detfs, nfs, adfs;
	detms, nms;
	detms, nms, adms.

npp --> detmp, nmp;
	detmp, nmp, admp;
	detfp, nfp;
    detfp, nfp, adfp.

vps --> vts, nps;
    vts, npp.

vpp --> vtp, nps;
    vtp, npp.


% Terminals
% Determinants
detms --> [Word], {lex(Word, detms)}.
detmp --> [Word], {lex(Word, detmp)}.
detfs --> [Word], {lex(Word, detfs)}.
detfp --> [Word], {lex(Word, detfp)}.
% nouns
nms --> [Word], {lex(Word, nms)}.
nmp --> [Word], {lex(Word, nmp)}.
nfs --> [Word], {lex(Word, nfs)}.
nfp --> [Word], {lex(Word, nfp)}.
% verbs
vtp --> [Word], {lex(Word, vtp)}.
vts --> [Word], {lex(Word, vts)}.
% adjectives
adfs --> [Word], {lex(Word, adfs)}.
adms --> [Word], {lex(Word, adms)}.
adfp --> [Word], {lex(Word, adfp)}.
admp --> [Word], {lex(Word, admp)}.