import asyncio
import logging
import time
import websockets
#Inicializacion Objeto
#Realizar conexion
#Ejecutar cmd
#Para asegurar la correcta ejecucion - loop.run_until_complete(cmd)
class WebsocketConnector():
    #Que variables globales necesitare
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.URL = f"ws://{self.ip_address}:{port}"
        self.conn = None
        self.loop = asyncio.get_event_loop()

    def get_connection(self):
        conn = None
        retry_count = 10
        while conn is None and retry_count > 0:
            try:
                logging.debug(f"Establishing connection with {self.URL}")
                conn = connect(self.URL)
            except Exception as ex:
                logging.warning(f"Failed to establish connection.. retrying again after 1 min. {ex}")
                time.sleep(60)
                conn = None
                retry_count -= 1
        if conn is None:
            logging.error(f"Failed to establish connection with {self.URL}")
        return conn

    def execute_command(self,command):
        try:
            return self.loop.run_until_complete(self.__execute_command(command))
        except Exception as ex:
            logging.warning(f"Failed to execute {command =}.")
        return False
    async def __execute_command(self, command):
        if self.conn is None:
            logging.debug(f"Connection object is None. Creating connection with {self/URL}")
            self.conn = await self.get_connection()
        await self.conn.send(command)
        return await self.conn.recv()
