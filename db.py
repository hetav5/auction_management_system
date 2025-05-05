import mysql.connector
from mysql.connector import Error
from datetime import datetime


class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'  # Replace with your MySQL username
        self.password = 'Hero@2002'  # Replace with your MySQL password
        self.database = 'auctiondb'
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to the database successfully.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    # User methods without hashing (plaintext passwords)
    def add_user(self, username, password, email, first_name, last_name, phone_number, address):
        cursor = self.connection.cursor()
        try:
            query = """
                INSERT INTO USER (username, password, email, first_name, last_name, phone_number, address)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (username, password, email,
                           first_name, last_name, phone_number, address))
            self.connection.commit()
            return True
        except mysql.connector.IntegrityError:
            return False
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
        finally:
            cursor.close()

    def verify_user(self, username, password):
        cursor = self.connection.cursor()
        try:
            query = "SELECT user_id FROM USER WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error verifying user: {e}")
            return None
        finally:
            cursor.close()

    def verify_admin(self, username, password):
        if not self.connection or not self.connection.is_connected():
            self.connect()
        if not self.connection:
            print("Database connection is not available.")
            return None

        cursor = self.connection.cursor()
        try:
            query = "SELECT admin_id FROM ADMIN WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error verifying admin: {e}")
            return None
        finally:
            cursor.close()

    def get_all_users(self):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT user_id, username, email, first_name, last_name, phone_number, address FROM USER")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []
        finally:
            cursor.close()

    def get_user_by_id(self, user_id):
        """Get user details by user ID"""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT user_id, username, email, first_name, last_name, 
                    phone_number, address 
                FROM USER 
                WHERE user_id = %s
            """
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error fetching user data: {e}")
            return None
        finally:
            cursor.close()

    def update_user(self, user_id, username, password, email, first_name, last_name, phone_number, address):
        cursor = self.connection.cursor()
        try:
            query = """
                UPDATE USER SET username = %s, password = %s, email = %s, first_name = %s, last_name = %s, phone_number = %s, address = %s 
                WHERE user_id = %s
            """
            cursor.execute(query, (username, password, email,
                           first_name, last_name, phone_number, address, user_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            cursor.close()

    def update_user_self(self, user_id, first_name, last_name, phone_number, address):
        cursor = self.connection.cursor()
        try:
            query = """
                UPDATE USER SET first_name = %s, last_name = %s, phone_number = %s, address = %s WHERE user_id = %s
            """
            cursor.execute(query, (first_name, last_name,
                           phone_number, address, user_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating user profile: {e}")
            return False
        finally:
            cursor.close()

    def delete_user(self, user_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM USER WHERE user_id = %s", (user_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            cursor.close()

    def delete_user_self(self, user_id):
        return self.delete_user(user_id)

    # Auction methods
    def get_all_auctions(self):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM AUCTION")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching auctions: {e}")
            return []
        finally:
            cursor.close()

    def get_active_auctions(self):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM AUCTION WHERE status = 'active'")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching active auctions: {e}")
            return []
        finally:
            cursor.close()

    def add_auction(self, title, description, start_date, end_date, reserve_price, auctioneer_id, status="active"):
        cursor = self.connection.cursor()
        try:
            query = """
                INSERT INTO AUCTION (title, description, start_date, end_date, reserve_price, auctioneer_id, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (title, description, start_date,
                           end_date, reserve_price, auctioneer_id, status))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error adding auction: {e}")
            return False
        finally:
            cursor.close()

    def update_auction(self, auction_id, title, description, start_date, end_date, reserve_price, current_bid, auctioneer_id, status):
        cursor = self.connection.cursor()
        try:
            query = """
                UPDATE AUCTION SET title = %s, description = %s, start_date = %s, end_date = %s, reserve_price = %s, current_bid = %s, auctioneer_id = %s, status = %s WHERE auction_id = %s
            """
            cursor.execute(query, (title, description, start_date, end_date,
                           reserve_price, current_bid, auctioneer_id, status, auction_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating auction: {e}")
            return False
        finally:
            cursor.close()

    def delete_auction(self, auction_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "DELETE FROM AUCTION WHERE auction_id = %s", (auction_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting auction: {e}")
            return False
        finally:
            cursor.close()

    # Bidder and Bid methods
    def get_bidder_id_by_user(self, user_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT bidder_id FROM BIDDER WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                cursor.execute(
                    "INSERT INTO BIDDER (user_id) VALUES (%s)", (user_id,))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            print(f"Error getting/creating bidder_id: {e}")
            return None
        finally:
            cursor.close()

    def place_bid(self, user_id, auction_id, bid_amount):
        cursor = self.connection.cursor()
        try:
            bidder_id = self.get_bidder_id_by_user(user_id)
            if not bidder_id:
                print("Failed to get or create bidder_id")
                return False

            cursor.execute(
                "SELECT current_bid FROM AUCTION WHERE auction_id = %s", (auction_id,))
            result = cursor.fetchone()
            if not result:
                print("Auction not found")
                return False
            current_bid = result[0]
            if bid_amount <= current_bid:
                print("Bid amount too low")
                return False

            cursor.execute("INSERT INTO BID (bidder_id, auction_id, bid_amount) VALUES (%s, %s, %s)",
                           (bidder_id, auction_id, bid_amount))
            cursor.execute(
                "UPDATE AUCTION SET current_bid = %s WHERE auction_id = %s", (bid_amount, auction_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error placing bid: {e}")
            return False
        finally:
            cursor.close()

    def get_latest_bid(self):
        """Fetch the latest bid details from the BID table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()
        if not self.connection:
            print("Database connection is not available.")
            return None

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT b.bid_id, b.bid_amount, b.auction_id, u.username AS bidder_name
                FROM BID b
                JOIN BIDDER br ON b.bidder_id = br.bidder_id
                JOIN USER u ON br.user_id = u.user_id
                ORDER BY b.bid_time DESC
                LIMIT 1
            """
            cursor.execute(query)
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error fetching latest bid: {e}")
            return None
        finally:
            cursor.close()

    def get_all_bids(self):
        """Fetch all bids from the BID table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT b.bid_id, b.auction_id, u.username AS bidder_name, b.bid_amount, b.bid_time
                FROM BID b
                JOIN BIDDER br ON b.bidder_id = br.bidder_id
                JOIN USER u ON br.user_id = u.user_id
                ORDER BY b.bid_time DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching bids: {e}")
            return []
        finally:
            cursor.close()

    # Auction Rules
    def get_auction_rules(self, auction_id):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT rule_description FROM AUCTION_RULES WHERE auction_id = %s", (auction_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching auction rules: {e}")
            return []
        finally:
            cursor.close()

    def get_all_items(self):
        """Fetch all items from the item table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT item_id, name, description, category_id, starting_price, auction_id
                FROM item
                ORDER BY item_id ASC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching items: {e}")
            return []
        finally:
            cursor.close()

    def get_auction_history(self):
        """Fetch all auction history records."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT history_id, auction_id, winner_id, final_bid_amount, end_time
                FROM auction_history
                ORDER BY end_time DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching auction history: {e}")
            return []
        finally:
            cursor.close()

    def get_all_auctioneers(self):
        """Fetch all auctioneers from the auctioneer table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT auctioneer_id, name, contact_info
                FROM auctioneer
                ORDER BY name ASC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching auctioneers: {e}")
            return []
        finally:
            cursor.close()

    def get_all_payments(self):
        """Fetch all payments from the payment table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT payment_id, bidder_id, auction_id, amount, payment_date, payment_method
                FROM payment
                ORDER BY payment_date DESC
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching payments: {e}")
            return []
        finally:
            cursor.close()

    def delete_item(self, item_id):
        """Delete an item from the item table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM item WHERE item_id = %s"
            cursor.execute(query, (item_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting item: {e}")
            return False
        finally:
            cursor.close()

    def update_item(self, item_id, name, description, category_id, starting_price, auction_id):
        """Update an item in the item table."""
        if not self.connection or not self.connection.is_connected():
            self.connect()

        cursor = self.connection.cursor()
        try:
            query = """
                UPDATE item
                SET name = %s, description = %s, category_id = %s, starting_price = %s, auction_id = %s
                WHERE item_id = %s
            """
            cursor.execute(query, (name, description, category_id,
                           starting_price, auction_id, item_id))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating item: {e}")
            return False
        finally:
            cursor.close()
