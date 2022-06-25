#!/usr/bin/env python3

import my_app

if __name__ == "__main__":
    config = {
        'storage': 'storage_memory',
        'namespace': 'default'
    }
    app = my_app.create_app(config_params=config)
    app.run()
