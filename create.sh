aws cloudformation create-stack \
--stack-name $1 \
--parameters file://$3 \
--template-body file://$4 \
--region us-west-2 \
