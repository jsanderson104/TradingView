<?php
// Author: Justin Sanderson
// Purpose: This PHP page should be served up over HTTPS to meet TradingView requirements (TV will not webhook to port 80 for security reasons). It ingests a JSON payload from TV then sends that JSON data to a Python script that sends a TXT message to my phone.
// Needs work:
// 1. Test webhook json ingestion
// 2. Determine best format to send to Mail python script. 

header('Content-Type: application/json');
define('WEBHOOK_PASSPHRASE', 'secret'); // Note: This is a simple security measure to ensure that no one can access the site w/o knowing a "password".

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method Not Allowed']);
    exit;
}

$rawInput = file_get_contents('php://input');
$data = json_decode($rawInput, true);

if ($data === null) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'Invalid JSON payload']);
    exit;
}

if (!isset($data['passphrase']) || $data['passphrase'] !== WEBHOOK_PASSPHRASE) {
    http_response_code(401);
    echo json_encode(['status' => 'error', 'message' => 'Unauthorized']);
    exit;
}

$action = "Price has moved on symbol";
$symbol = "SPX";

#$cmd = "/var/www/html/sendmail.py;
#$output = shell_exec(cmd);


// 7. Respond with a 200 OK success message
http_response_code(200);
echo json_encode(['status' => 'success', 'message' => 'Alert received successfully']);

?>
