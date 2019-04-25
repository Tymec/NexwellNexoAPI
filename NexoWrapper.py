from NexoVisionClient import NexoVisionClient
import ujson


class NexoWrapper:
    def __init__(self, ip_address, password):
        self.nexo_client = NexoVisionClient(ip_address)
        self.nexo_client.initialize_connection(password)
        self.nexo_client.clear_server_buffer_queue()
        
        self.resources = {}
        
    def get_state(self, name):
        state = self.nexo_client.system_c(name, '?')
        return state
    
    def set_state(self, name, state):
        if state is not 1 and state is not 0:
            self.nexo_client.log("Wrong value", 'error')
            return
        self.nexo_client.system_c(name, state)
        new_state = self.get_state(name)
        return new_state

    def scan_test(self, devices_to_scan):
        import time
        vifte = False
        i = 0
        start = time.time()
        while not vifte:
            if i > devices_to_scan:
                break
            self.get_state('vifte bad')
            i += 1
        self.nexo_client.log(f"Took {time.time() - start:.2} seconds to finish scanning", 'info')
        return

    def import_resources_from_file(self):
        with open('resources.json', 'r') as f:
            self.resources = ujson.load(f)
        
    def debug(self):
        state = self.get_state('GANG term')
        print(state)
        self.nexo_client.disconnect()
        
if __name__ == "__main__":
    nexo_wrapper = NexoWrapper('192.168.1.75', '1510')
    nexo_wrapper.debug()