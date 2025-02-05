let baseUrl = document.querySelector('.url').value;
let key = document.querySelector('.key').value;
let value = document.querySelector('.value').value;
let button = document.querySelector('#process')
let vehicles;
let url;
let error = document.querySelector('#error');
// keys
const keys = ['Brand', 'Model', 'Year', 'Engine_Size', 'Fuel_Type', 'Transmission', 'Mileage', 'Doors', 'Owner_Count', 'Price']

// create table row ( tr )
function create_table_row() {
    return document.createElement("tr");
}

// create table data with its content ( td )
function create_table_data(content) {
    let td = document.createElement('td')
    td.textContent = content

    return td
}

// create table head ( th )
function create_table_head(content) {
    let th = document.createElement('th')
    th.setAttribute('scope', 'col')
    th.textContent = content

    return th
}

// table tag
const table = document.querySelector('#table')

// table headers
const thead = document.createElement('thead')
// create row
let tr = create_table_row()

let th = create_table_head('#')
tr.appendChild(th)
for (const key of keys) {
    // create table headers
    let th = create_table_head(key)
    // add to the table row inside the thead
    tr.appendChild(th)
}

// add the populated table row to the thead tag
thead.appendChild(tr)

// add the thead tag to the table
table.appendChild(thead)

// create table body
let tbody = document.createElement('tbody')

async function fetchVehicles() {
    try {
        // get data from the given url
        const response = await fetch(url);

        // check the response status
        // throw an error if the status is not ok or 200
        if (!response.ok) throw new Error("Failed to fetch vehicles");

        // get the vehicle data in a JavaScript object
        vehicles = await response.json();

        if (vehicles.length === 0) {
            console.log(key.value, value.value);
            error.textContent = `There is no such key=${key.value} or value=${value.value}`
            return
        }

        // Populate table with vehicle data
        let vehicle_counter = 1
        vehicles.forEach(vehicle => {
            let td = create_table_data(vehicle_counter)
            const row = create_table_row()
            row.appendChild(td)
            for (const key of keys) {

                // format the vehicle price as a currency
                if (key == 'Price') {
                    const formattedAmount = new Intl.NumberFormat('en-US', {
                        style: 'currency',
                        currency: 'USD',
                    }).format(parseFloat(vehicle[key]))

                    // add the formatted number
                    td = create_table_data(formattedAmount)
                    row.appendChild(td)
                    continue;
                }

                // add td to tr
                td = create_table_data(vehicle[key])
                row.appendChild(td);
            }
            ++vehicle_counter;
            tbody.appendChild(row)
        });
        table.appendChild(tbody);
    } catch (error) {
        console.error("Error:", error);
    }
}


button.addEventListener('click', function (e) {
    url = `${baseUrl}/${key}/${value}`
    // if (baseUrl.value == undefined || key.value == undefined || value.value == undefined) {
    //     console.log(baseUrl.value, key.value, value.value);
    //     url = `http://localhost:8000/vehicles`
    // } else {
    //     url = `${baseUrl}/${key}/${value}`
    // }

    // Fetch vehicles when page loads
    fetchVehicles();

    baseUrl.value = ''
    key.value = ''
    value.value = ''
});