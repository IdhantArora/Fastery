create database if not exists market_management;
show databases;
use market_management;

create table if not exists customer(customer_id int auto_increment primary key, customer_name varchar(50) not null unique ,customer_phone varchar(12) not null, customer_email varchar(255) not null, customer_password varchar(250) not null,customer_address varchar(255) not null,customer_card varchar(12), c_pass varchar(50) not null default "pass", is_Blocked bool default false);
create table if not exists orders(order_id int auto_increment primary key, order_date date not null, order_time time not null, order_amount int not null check (order_amount>0),items_total int not null check (items_total>0),customer_id int,foreign key(customer_id) references customer(customer_id));
create table if not exists transactions(trans_id int auto_increment primary key, trans_type char not null,trans_date date not null, trans_time time not null, trans_status char not null,trans_amount int not null check (trans_amount>0),order_id int,foreign key(order_id) references orders(order_id));
create table if not exists shipper(shipper_id int auto_increment primary key, shipper_pin int not null,shipper_name varchar(50) not null, shipper_phone varchar(12) not null, shipper_address varchar(100) not null);
create table if not exists supply(order_id int, shipper_id int, primary key(order_id,shipper_id), foreign key(order_id) references orders(order_id),foreign key(shipper_id) references shipper(shipper_id), delivery_date date, supply_status char not null);
create table if not exists category(cat_id int auto_increment primary key, cat_name varchar(20) not null);
create table if not exists products(prod_id int auto_increment primary key, prod_name varchar(40) not null, cat_id int, foreign key(cat_id) references category(cat_id), quantity int not null check (quantity>0), price int not null check (price>0));
create table if not exists warehouse(house_id int auto_increment primary key, house_address varchar(50) not null, pincode int not null);
create table if not exists manager(manager_id int auto_increment primary key, house_id int, foreign key(house_id) references warehouse(house_id), manager_name varchar(30) not null, manager_phone varchar(12) not null, manager_address varchar(50) not null, manager_pass varchar(20) not null);
create table if not exists inventory(prod_id int not null,house_id int not null, primary key(prod_id,house_id), foreign key(prod_id) references products(prod_id), foreign key(house_id) references warehouse(house_id), quantity int not null check (quantity>0));
create table if not exists collects(order_id int primary key, foreign key(order_id) references orders(order_id), collect_date date not null, shipper_id int not null, house_id int not null, foreign key(house_id) references warehouse(house_id) ,foreign key(shipper_id) references shipper(shipper_id));
create table if not exists cart(customer_id int, prod_id int, quantity int not null, primary key (customer_id,prod_id), foreign key(customer_id) references customer(customer_id), foreign key(prod_id) references products(prod_id));
create table if not exists purchases(order_id int, prod_id int, quantity int, primary key (order_id,prod_id), foreign key(order_id) references orders(order_id), foreign key(prod_id) references products(prod_id));
create table if not exists failedLogin(customer_name varchar(50), foreign key(customer_name) references customer(customer_name), attempts int default 0);


DELIMITER $$
CREATE TRIGGER update_products_after_purchase
AFTER INSERT ON purchases
FOR EACH ROW
BEGIN
  DECLARE prod_id1 INT;
  SET prod_id1 = NEW.prod_id;

  UPDATE products
  SET quantity = quantity - NEW.quantity
  WHERE prod_id = prod_id1;
END $$
DELIMITER ;

-- use market_management;
DELIMITER $$
CREATE TRIGGER update_failedLogins
AFTER UPDATE ON failedLogin
FOR EACH ROW
BEGIN
  DECLARE att INT;
  SET att = NEW.attempts;

   IF att >= 3 THEN
	UPDATE customer
	SET is_Blocked = true
	WHERE customer_name = NEW.customer_name;
	END IF;
END $$
DELIMITER ;


insert into customer(customer_name, customer_phone, customer_email, customer_password, customer_address, customer_card) values
("Harsh Rawat", 9999999990, "harsh22202@iiitd.ac.in", "harshPass", "15, Indrapuram, Noida, UP, India", NULL),
("Idhant Arora", 9999999991, "idhant22220@iiitd.ac.in", "idhantPass", "10, JagatPuri, Delhi, India", 367578789999),
("Tanmay Khatri", 9999999992, "tanmay22534@iiitd.ac.in", "tanmayPass", "12, Nirman Vihar, Delhi, India", 454567452323),
("Nangia Nangia", 9999999993, "nangia@gmail.com", "nangiaPass", "55, Laxmi Nagar, Delhi, India", NULL),
("Siddharth Joshi", 9876543210, "siddhartha@gmail.com", "siddharthaPass", "23, Park Avenue, New Delhi, India", 567898765657),
("Rajesh Gupta", 8888888888, "rajesh@gmail.com", "rajeshPass", "44, Navi Mumbai, Mumbai, India", 454578092345),
("Cody Rhodes", 7777777777, "cody@gmail.com", "codyPass", "Atlanta, Georgia, USA", 563890678945),
("Amit Verma", 6666666666, "amit@gmail.com", "amitPass", "12, Punjabi Bagh, Delhi, India", NULL),
("Vikram Pandey", 5555555555, "vikram@gmail.com", "vikramPass", "67, Nanjing Road, Delhi, India", NULL),
("Ajay Jha", 4444444444, "ajay@gmail.com", "ajayPass", "69, Malwa, Punjab", 749687462856);

insert into failedLogin(customer_name) values
("Harsh Rawat"),
("Idhant Arora"),
("Tanmay Khatri"),
("Nangia Nangia"),
("Siddharth Joshi"),
("Rajesh Gupta"),
("Cody Rhodes"),
("Amit Verma"),
("Vikram Pandey"),
("Ajay Jha");


insert into orders (order_date, order_time, order_amount, items_total, customer_id) values
("2024-01-22", "19:30:10", 2000, 4, 1),
("2024-01-23", "10:15:30", 1800, 3, 2),
("2024-01-24", "14:20:45", 2200, 6, 3),
("2024-01-25", "09:00:00", 2500, 11, 4),
("2024-01-26", "16:45:15", 1900, 2, 5),
("2024-01-27", "12:30:20", 2100, 4, 6),
("2024-01-27", "11:10:05", 2400, 8, 7),
("2024-01-29", "13:00:40", 2300, 3, 8),
("2024-01-30", "15:55:55", 2050, 5, 9),
("2024-01-31", "18:40:10", 1980, 2, 10);


insert into transactions (trans_type, trans_date, trans_time, trans_status,trans_amount, order_id) values
('C', "2024-01-22", "12:23:34", "P", 2000, 1),
('O', "2024-01-23", "14:45:20", "U", 1800, 2),
('O', "2024-01-24", "09:10:15", "U", 2200, 3),
('C', "2024-01-25", "18:30:05", "P", 2500, 4),
('O', "2024-01-26", "11:55:30", "P", 1900, 5),
('C', "2024-01-27", "15:20:40", "P", 2100, 6),
('C', "2024-01-28", "13:40:00", "U", 2400, 7),
('C', "2024-01-29", "16:15:10", "P", 2300, 8),
('C', "2024-01-30", "10:05:25", "U", 2050, 9),
('O', "2024-01-31", "17:00:50", "P", 1980, 10);


insert into shipper(shipper_pin,shipper_name,shipper_phone,shipper_address) values
(110092, "Ajay Sharma", "9898989898", "26-A, Karkardooma, Delhi, India"),
(110093, "Rajesh Verma", "9876543210", "12-B, Lajpat Nagar, New Delhi, India"),
(110094, "Anuj Gupta", "8765432109", "7/3, Malviya Nagar, Jaipur, India"),
(110095, "Amit Kumar", "7654321098", "15, MG Road, Bangalore, India"),
(110096, "Praveen Singh", "6543210987", "22, Park Street, Kolkata, India"),
(110097, "Sanjay Patel", "9432109876", "5, Gandhi Road, Chennai, India"),
(110098, "Ashutosh Sharma", "9321098765", "9, Civil Lines, Lucknow, India"),
(110099, "Vikram Yadav", "8210987654", "3, Rajpur Road, Dehradun, India"),
(110100, "Naveen Kapoor", "9109876543", "18, MG Marg, Gangtok, India"),
(110101, "Rahul Das", "8898765432", "11, Marine Drive, Mumbai, India");


insert into warehouse (house_address,pincode) values
("123, Main Street",  110092),
("456, Royal Avenue",  110093),
("789, Oak Drive",  110094),
("101, Pine Street",  110095),
("202, Park Lane",  110096),
("303, MG Road",  110097),
("404, Birch Boulevard", 110098),
("505, JLN Street",  110099),
("606, Star Avenue",  110100),
("707, BJ Road",  110101);


insert into manager(house_id,manager_name,manager_phone,manager_address,manager_pass) values
(1,"Jay Shah",9234567890,"123, Main St", "password123"),
(2,"Virat Sharma",9345678901,"456, Parwana Road ","pass1234"),
(3,"Rohit Kohli", 9456789012, "789, Pushta Road","pass4567"),
(4,"Ravi Arora",9567890123,"101, Bhagat Singh Marg","password456"),
(5,"Aditya Vells",9678901234,"202, MaheshPur","pass7890"),
(6, "Yash Kumar",9789012345,"303, MG Road","password789"),
(7,"Bhavya Hule",9890123456,"404, Vikas Marg","pass12345"),
(8,"Ashi Sethi",8901234567,"505, Lawrence Road","password6789"),
(9,"Aishwarya Khurana",9012345678,"606, Jag Path","pass5678"),
(10,"Khushi Arora",9123456789,"707, Dogra Marg","password890");


INSERT INTO category(cat_name) VALUES
('Namkeen'), ('Energy Drink'), ('Ice Cream'), ('Snack'), ('Beverage'), 
('Chips'), ('Soda'), ('Cookies'), ('Cake'), ('Candy');


INSERT INTO products(prod_name,cat_id,quantity,price) VALUES
("Coke 250ml", 2, 1000, 20),
("Britannia Cake", 9, 1200, 25),
("Alpenlibe Candies 100pk", 10, 800, 50),
("Bisleri Soda 500ml", 7, 1500, 10),
("Butterscotch Ice Cream", 3, 1100, 20),
("Bikaji Bhujia 100gm", 1, 900, 20),
("Maggi", 4, 1300, 12),
("Amul Lassi 100ml", 5, 1000, 20),
("Lays Blue", 6, 850, 10),
("Good Day Butter", 8, 1400, 10),
("Lays Green", 6, 1, 10);


INSERT INTO supply(order_id, shipper_id, delivery_date, supply_status) VALUES
(1,10, "2024-01-24", 'D'),
(2, 9, "2024-01-25", 'D'),
(3, 8, "2024-01-26", 'D'),
(4, 7, NULL, 'U'),
(5, 6, NULL, 'U'),
(6, 5, NULL, 'U'),
(7, 4, NULL, 'U'),
(8, 3, NULL, 'U'),
(9, 2, NULL, 'U'),
(10, 1, NULL, 'U');


insert into inventory(prod_id,house_id,quantity) values
(1,8,900),(2,4,1000),(3,5,1100),(4,6,1300),(5,7,1000),
(6,1,850),(7,2,1500),(8,10,1400),(9,9,1200),(10,3,800);


insert into collects(order_id, collect_date, shipper_id, house_id) values
(1,"2024-01-23",10,5),
(2,"2024-01-24",9,6),
(3,"2024-01-25",8,7),
(4,"2024-01-26",7,8),
(5,"2024-01-27",6,9),
(6,"2024-01-28",5,10),
(7,"2024-01-28",4,1),
(8,"2024-01-29",3,2),
(9,"2024-01-30",2,3),
(10,"2024-01-31",1,4);

insert into cart(customer_id,prod_id, quantity) values
(1,3,1),
(1,10,3),
(1,4,5),
(5,6,2),
(5,4,1),
(9,3,23),
(9,4,4),
(8,5,6),
(7,9,9),
(6,1,8);

insert into purchases(order_id, prod_id, quantity) values
(1,2,1),
(1,4,1),
(2,5,2),
(2,8,1),
(3,3,2),
(3,6,4),
(4,7,7),
(4,2,4),
(5,6,1),
(5,9,1); 

 

-- SQL QUERIES FOR DEADLINE-4

select customer_id C_Id,sum(c.quantity*p.price) Amount from cart c join products p where c.prod_id = p.prod_id group by customer_id; -- calculating total amount from cart of a user

-- update inventory i,products p set i.quantity = i.quantity+100,p.quantity = p.quantity+100 where i.prod_id = 1 and i.house_id = 8; -- a manager updating quantity in his warehouse

-- update products p join cart c on p.prod_id = c.prod_id set p.quantity = p.quantity - c.quantity where c.customer_id = 1; -- deducting quantity of product in cart when order is placed

select customer_id, sum(order_amount) as sales from orders group by customer_id order by sales desc limit 3; -- selecting top 3 buyer of all time

select shipper_name,shipper_phone, customer_name, s2.order_id from shipper as s1 join supply as s2 on s1.shipper_id = s2.shipper_id join orders as o on s2.order_id = o.order_id join customer as c on c.customer_id = o.customer_id where s2.supply_status = 'U'; -- shipper and user details with undelivered orders

select pro.prod_name, pur.quantity, o.order_date, s.supply_status from purchases as pur join products as pro on pur.prod_id = pro.prod_id join orders as o on pur.order_id = o.order_id join supply as s on s.order_id = o.order_id where o.customer_id = 1; -- items purchased by users in history along with delivery status

select house_id, prod_id, quantity from inventory where quantity < 1000 and house_id = 1; -- selecting all items whose quantity is less than 1000 in warehouse
 
select sum(quantity),prod_id from purchases group by prod_id; -- total items sold of each item

select sum(trans_amount),year(trans_date) from transactions where trans_type = 'O' and trans_status = 'P' group by year(trans_date); -- total amount received online each year
 
-- update products as p set p.price = p.price + 5 where p.cat_id = 1; -- updating price of products of a perticular category

-- queries which check contraints

-- update products set price = -1 where prod_id = 1;

-- update inventory set quantity = -100 where prod_id = 2;
 