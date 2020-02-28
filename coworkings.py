CW1 = {
    "name": "CREC Coworking Poble Sec",
    "description": "Bla bla bla pole pole pole fail fail fail.",
    "street": "Blesa 27",
    "city": "Barcelona",
    "phone": "931 165 585",
    "website": "https://www.crec.cc",
    "social_networks": {
        "facebook": "https://www.facebook.com/CRECbcn",
        "twitter": "https://twitter.com/CRECbcn"
    },
    "services": {"Sala de reuniones", "Recepción", "Pizarra", "Proyector", "Televisor",
                 "Cocina", "Aire acondicionado", "Alarma", "Internet", "Impresora",
                 "Prueba gratuita", "Escáner"},

    "desks": {
        0: {"name": "Mesa fija", "type": "dedicated", "price": 235, "stay_time": "monthly", "hours": "full-time"},
        1: {"name": "Mesa flexible", "type": "hot", "price": 185, "stay_time": "monthly", "hours": "full-time"},
        2: {"name": "Mesa flex part-time", "type": "hot", "price": 120, "stay_time": "monthly", "hours": "part-time"},
        3: {"name": "Mesa flexible", "type": "hot", "price": 60, "stay_time": "10 days", "hours": "full-time"},
    },

    "offices": {
        0: {"name": "Oficina Sala A", "capacity": 32, "price": 3200},
        1: {"name": "Oficina Daenerys", "capacity": 6, "price": 800}
    },

    "meetings": {
        0: {"name": "Reuniones CC", "capacity": 5, "price": 12},  # especificar euros/hora
    },

    "events": {
        0: {"name": "Sala de eventos", "capacity": 100, "price": 50},
    }

}

CW2 = {
    "name": "Espacio Meraki",
    "description": "Bla bla bla pole pole pole fail fail fail.",
    "street": "Comptes de Bell-lloc 161-187",
    "city": "Barcelona",
    "phone": "611 171 471",
    "website": "https://www.holameraki.com",
    "social_networks": {
        "facebook": "http://facebook.com/meraki.hola/",
        "instagram": "https://www.instagram.com/meraki.hola/"
    },
    "services": {"Sala de reuniones", "Recepción", "Pizarra", "Proyector", "Televisor",
                 "Cocina", "Aire acondicionado", "Alarma", "Domiciliación fiscal", "Café"
                 "Internet", "Mascotas permitidas", "Impresora", "Prueba gratuita", "Escáner"},

    "desks": {
        0: {"name": "Mesa fija", "type": "dedicated", "price": 200, "stay_time": "monthly", "hours": "full-time"},
        1: {"name": "Mesa flexible", "type": "hot", "price": 165, "stay_time": "monthly", "hours": "full-time"},
        2: {"name": "Mesa flexible", "type": "hot", "price": 45, "stay_time": "5 days", "hours": "full-time"},
    },

    "offices": {
        0: {"name": "Despacho privado", "capacity": 7, "price": 1100},
    },

    "meetings": {
        0: {"name": "Sala Meraki", "capacity": 6, "price": 12},  # especificar euros/hora
    },

    "events": {
        0: {"name": "Eventos Meraki", "capacity": 75, "price": 60},
    }

}
