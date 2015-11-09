/* Goods Details */
CREATE TABLE IF NOT EXISTS t_goods (
       c_goods_code CHAR(10) PRIMARY KEY,
       c_goods_jancode CHAR(13),
       c_goods_name VARCHAR(100),
       c_goods_maker VARCHAR(100),
       c_goods_country VARCHAR(100),
       c_goods_explain VARCHAR(500)
       ) DEFAULT CHARACTER SET 'utf8';

/* Goods */
CREATE TABLE IF NOT EXISTS t_sales (
       c_sales_entry_no BIGINT AUTO_INCREMENT PRIMARY KEY,
       c_sales_code CHAR(10)  NOT NULL,
       c_sales_period VARCHAR(7) NOT NULL,
       c_sales_price INT,
       c_sales_totalprice INT,
       c_sales_order_no CHAR(6),
       c_sales_standard VARCHAR(100),
       c_sales_calorie VARCHAR(100),
       FOREIGN KEY (c_sales_code) REFERENCES t_goods (c_goods_code)
       ) DEFAULT CHARACTER SET 'utf8';

/*
-- For test
SELECT * FROM t_sales LEFT OUTER JOIN t_goods ON t_sales.c_sales_code=t_goods.c_goods_code;
*/
