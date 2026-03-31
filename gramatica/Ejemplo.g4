grammar Ejemplo;

s : 'a' b c EOF ;

b : 'b' 'bas'
  | 'big' c 'boss'
  ;

c : 'c'
  |
  ;

WS : [ \t\r\n]+ -> skip ;
