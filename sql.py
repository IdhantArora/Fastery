import mysql.connector

def update_inventory(host, user, password, database):
    prod_id=str(int(input()))
    qty=str(int(input()))
    house_id=str(int(input()))
    command="update inventory i,products p set i.quantity = i.quantity+{},p.quantity = p.quantity+{} where i.prod_id = {} and i.house_id = {};".format(qty,prod_id,house_id)
    execute_mysql_command(host,user,password,database,command)

def deduct_after_adding_to_cart(host, user, password, database):
    customer_id=str(int(input()))
    command="update products p join cart c on p.prod_id = c.prod_id set p.quantity = p.quantity - c.quantity where c.customer_id = {};".format(customer_id)
    execute_mysql_command(host,user,password,database,command)

def get_info_about_delivery(host, user, password, database):
    status=input()
    c="select shipper_name,shipper_phone, customer_name, s2.order_id from shipper as s1 join supply as s2 on s1.shipper_id = s2.shipper_id join orders as o on s2.order_id = o.order_id join customer as c on c.customer_id = o.customer_id where s2.supply_status = '{}';".format(status)
    execute_mysql_command(host,user,password,database,c)

def order_history(host,user,password,database,command):
    id=str(int(input()))
    c="select pro.prod_name, pur.quantity, o.order_date, s.supply_status from purchases as pur join products as pro on pur.prod_id = pro.prod_id join orders as o on pur.order_id = o.order_id join supply as s on s.order_id = o.order_id where o.customer_id = {};".format(id)
    execute_mysql_command(host,user,password,database,c)

def qty_warehouse(host,user,password,database):#ok
    qty = str(int(input("Enter the quantity threshold: ")))
    id = str(int(input("Enter the house ID: ")))
    c = "SELECT house_id, prod_id, quantity FROM inventory WHERE quantity < {} AND house_id = {};".format(qty, id)
    execute_mysql_command(host,user,password,database,c)

def top_n_buyer(host,user,password,database):
    n=str(int(input()))
    c="select customer_id, sum(order_amount) as sales from orders group by customer_id order by sales desc limit {};".format(n)
    execute_mysql_command(host,user,password,database,c)


def update_price(host,user,password,database):#ok
    price=str(int(input()))
    id=str(int(input()))
    c="update products as p set p.price = p.price + {} where p.prod_id = {};".format(price,id)
    execute_mysql_command(host,user,password,database,c)

def execute_mysql_command(host, user, password, database, command):
    try:
        # Establish connection to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Execute the MySQL command
            cursor.execute(command)

            # If the query produces a result set, fetch or process the results
            if cursor.with_rows:
                result = cursor.fetchall()  # Fetch all rows if needed
                print(result)
                # Process the result as needed

            # Commit the transaction
            connection.commit()

            print("Command executed successfully.")

    except mysql.connector.Error as error:
        print("Error executing MySQL command:", error)

    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()



L=["select customer_id C_Id,sum(c.quantity*p.price) Amount from cart c join products p where c.prod_id = p.prod_id group by customer_id;",
"select sum(quantity),prod_id from purchases group by prod_id;",
"select sum(trans_amount),year(trans_date) from transactions where trans_type = 'O' and trans_status = 'P' group by year(trans_date);"]

host="localhost"
user="root"
password="sqlPass"
database="market_management"
qty_warehouse(host,user,password,database)