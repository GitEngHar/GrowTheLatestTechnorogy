echo "TB_NAME ?"
read tbname
export TB_NAME=$tbname
echo $TB_NAME

echo "DB_NAME ?"
read dbname
export DB_NAME=$dbname
echo $DB_NAME

echo "MYSQL_USER_NAME?"
read mysqlusername
export MYSQL_USER_NAME=$mysqlusername

echo "MYSQL_USER_PASSWORD?"
read mysqluserpassword
export MYSQL_USER_PASSWORD=$mysqluserpassword

echo "MYSQL_ENDPOINT?"
read mysqlendpoint
export MYSQL_ENDPOINT=$mysqlendpoint

echo "-e TB_NAME=$TB_NAME -e DB_NAME=$DB_NAME -e MYSQL_USER_NAME=$MYSQL_USER_NAME -e MYSQL_ENDPOINT=$MYSQL_ENDPOINT"