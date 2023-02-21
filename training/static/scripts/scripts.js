    async function request(url, data, csrftoken) {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
            },
        body: JSON.stringify(data)
        })
        const result = await response.text()
        return result
    }
    async function add_to_cart(id, token) {
        let input_amount = document.getElementById(id).querySelector('.pizza-buy').querySelector('.user-amount').value
        const operation_type=1
        const url = ''
        const data = {'selected-pizza': id, 'operation': 1, 'amount': Number(input_amount)}
        const csrftoken = token
        const result = await request(url, data, csrftoken, operation_type)
        if (result > 0){
            let block = document.getElementById(id)
            let label = block.querySelector('.pizza-buy').querySelector('.pizza-added')
            label.style.visibility="visible"
            label.querySelector('.added-label').innerHTML = `Добавлено (${result})  `
        }
    }

    async function delete_from_cart(id, token, page){
        const url = ''
        const data = {'selected-pizza': id, 'operation': 0, 'amount': 0}
        const csrftoken = token
        const from_page = page
        await request(url, data, csrftoken)
        let block = document.getElementById(id)
        let label = block.querySelector('.pizza-buy').querySelector('.pizza-added')
        label.style.visibility="hidden"
        if (from_page === 1){
            block.remove()
        }
    }

    async function get_orders(token){
        const url = ''
        const data = {'selected-pizza': 0, 'operation': 2, 'amount': 0}
        const csrftoken = token
        const answer = await request(url, data, csrftoken)
        JSON.parse(answer, function(k, v){
            let pizza_id = document.getElementById(k)
            if (v > 0){
                let label = pizza_id.querySelector('.pizza-buy').querySelector('.pizza-added')
                label.style.visibility="visible"
                label.querySelector('.added-label').innerHTML = `Добавлено (${v})  `
            }

        })

    }

    async function change_status(token, id){
        const url = ''
        const data = {'id': id}
        const csrftoken = token
        await request(url, data, csrftoken)
        location.reload()
    }