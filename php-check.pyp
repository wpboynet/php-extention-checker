<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Status Ekstensi & Fungsi PHP</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fdfdfd;
            margin: 0;
            padding: 0;
        }
        header {
            text-align: center;
            padding: 30px 0 10px;
        }
        header img {
            max-height: 80px;
        }
        h2, h3 {
            text-align: center;
            margin-top: 20px;
        }
        table {
            border-collapse: collapse;
            width: 90%;
            margin: 20px auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            background-color: #fff;
        }
        th, td {
            padding: 10px 14px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f5f5f5;
        }
        .active {
            color: green;
            font-weight: bold;
        }
        .inactive {
            color: red;
            font-weight: bold;
        }
        .info-box {
            max-width: 90%;
            margin: 20px auto;
            border: 1px solid #ccc;
            padding: 15px;
            font-size: 14px;
            line-height: 1.5;
        }
        .disabled-funcs {
            background: #fff3f3;
            border-color: #f0c0c0;
            color: #900;
        }
        .enabled-funcs {
            background: #f3fff3;
            border-color: #b0e0b0;
            color: #060;
        }
        footer {
            text-align: center;
            margin: 40px 0 20px;
            font-size: 14px;
            color: #666;
        }
        footer a {
            color: #0077cc;
            text-decoration: none;
        }
    </style>
</head>
<body>

<header>
    <img src="https://hosterbyte.com/wp-content/uploads/2024/06/Hosterbyte-Logo-WHMCS.png" alt="Hosterbyte Logo">
</header>

<h2>Status Ekstensi PHP</h2>

<table>
    <thead>
        <tr>
            <th>Nama Ekstensi</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <?php
        $extensions = [
            "amqp","apcu","b","bcmath","brotli","bz2","c","calendar","core","ctype","curl",
            "d","date","dba","dbase","dom","e","eio","enchant","exif","f","ffi","fileinfo",
            "filter","ftp","g","gd","gearman","geoip","geos","gettext","gmagick","gnupg",
            "grpc","h","hash","http","i","iconv","igbinary","imagick","imap","inotify","intl",
            "ioncube_loader","j","jsmin","json","l","ldap","libxml","luasandbox","lzf",
            "m","mailparse","mbstring","mcrypt","memcache","memcached","mongodb","msgpack",
            "mysqli","mysqlnd","n","nd_mysqli","nd_pdo_mysql","newrelic","o","oauth","oci8",
            "odbc","opcache","openssl","p","pcntl","pcre","pdf","pdo","pdo_dblib","pdo_firebird",
            "pdo_mysql","pdo_oci","pdo_odbc","pdo_pgsql","pdo_sqlite","pdo_sqlsrv","pgsql",
            "phalcon5","phar","posix","protobuf","pspell","psr","r","raphf","rar","readline",
            "redis","reflection","rrd","s","scoutapm","session","shmop","simplexml","snmp",
            "soap","sockets","sodium","solr","sourceguardian","spl","sqlite3","sqlsrv","ssh2",
            "standard","stats","swoole","sysvmsg","sysvsem","sysvshm","t","tideways_xhprof",
            "tidy","timezonedb","tokenizer","trader","u","uploadprogress","uuid","x","xdebug",
            "xml","xmlreader","xmlrpc","xmlwriter","xsl","y","yaf","yaml","yaz","z","zip","zlib","zmq"
        ];

        foreach ($extensions as $ext) {
            if (trim($ext) === "") continue;
            $loaded = extension_loaded($ext);
            echo "<tr>";
            echo "<td>{$ext}</td>";
            echo "<td class='" . ($loaded ? "active" : "inactive") . "'>"
                . ($loaded ? "✅ Aktif" : "❌ Tidak Aktif")
                . "</td>";
            echo "</tr>";
        }
        ?>
    </tbody>
</table>

<h3>Fungsi PHP yang Dinonaktifkan</h3>
<div class="info-box disabled-funcs">
    <?php
    $disabledRaw = ini_get('disable_functions');
    $disabledFunctions = array_filter(array_map('trim', explode(',', $disabledRaw)));
    echo $disabledRaw ? nl2br(htmlspecialchars($disabledRaw)) : "<em>Tidak ada fungsi yang dinonaktifkan.</em>";
    ?>
</div>

<h3>Fungsi PHP yang Diaktifkan</h3>
<div class="info-box enabled-funcs">
    <?php
    $allFunctions = get_defined_functions()['internal'];
    $enabledFunctions = array_diff($allFunctions, $disabledFunctions);
    echo count($enabledFunctions) . " fungsi aktif.";
    echo "<br><small>(Daftar sebagian: " . implode(', ', array_slice($enabledFunctions, 0, 30)) . " ...)</small>";
    ?>
</div>

<footer>
    &copy; <?= date('Y'); ?> by <a href="https://hosterbyte.com" target="_blank">hosterbyte.com</a>
</footer>

</body>
</html>
