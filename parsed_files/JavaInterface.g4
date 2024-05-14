// JavaInterface.g4

grammar JavaInterface;

compilationUnit: packageDeclaration? interfaceDeclaration EOF;

packageDeclaration: 'package' qualifiedName ';' ;

qualifiedName: IDENTIFIER ( '.' IDENTIFIER )* ;

interfaceDeclaration: 'public'? 'interface' IDENTIFIER interfaceBody ;

interfaceBody: '{' interfaceMember* '}' ;

interfaceMember: interfaceMethod ;

interfaceMethod: type IDENTIFIER '(' ')' ';' ;

type: 'String' ;

IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]* ;

WS: [ \t\r\n]+ -> skip ;

