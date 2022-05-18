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

lex(perras, nfp).

lex(bonita, adfs).
lex(bonitas, adfp).
lex(bonito, adms).
lex(bonitos, admp).

lex(ladra, vis).
lex(ladran, vip).

lex(muerde, vts).
lex(muerden, vtp).

% Terminals
% Determinants
det(G, N) -->
    Y=['det', G],
    atomic_list_concat(Y, N, X),
    [Word], {lex(Word, X)}.

% nouns
n(G, N) -->
    Y=['n', G],
    atomic_list_concat(Y, N, X),
    [Word], {lex(Word, X)}.

% verbs
v(T, N) -->
    Y=['v', T],
    atomic_list_concat(Y, N, X),
    [Word], {lex(Word, X)}.

% adjectives
ad(G, N) -->
    Y=['ad', G],
    atomic_list_concat(Y, N, X),
    [Word], {lex(Word, X)}.

% noun phrase
np(G, N) --> det(G, N), n(G, N);
	det(G, N), n(G, N), ad(G, N).

vp(_, N) --> v('t', N), n(_, N);
    v('i', N).

% Reglas del DCG
s --> np(_, N), vp(_, N).
