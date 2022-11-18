#!/bin/bash
#

for FILE in Tables/*.csv; do 
    echo "Importing $FILE"
    sqlite3 import_test.db << EOF
.mode csv
.import $FILE ${FILE%.csv}
EOF
done
    sqlite3 import_test.db ".backup backup_import_test.db"

