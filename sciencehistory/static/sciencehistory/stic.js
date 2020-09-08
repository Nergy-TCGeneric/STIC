function open_stic_wiki(name) {
        let wiki_viewer = document.getElementById("wiki_viewer")
        fetch(`http://stic.dothome.co.kr/w/api.php?action=parse&page=${name}&prop=text&formatversion=2&format=json`, {
            method: "GET",
            mode: 'cors',
            headers: {
                'Content-type': 'text/plain'
            }
        }).then(data => {
            data.json().then(result => {
                if (result['error'] != undefined) throw new Error("데이터를 받아오는 데 실패했습니다.")
                wiki_viewer.innerHTML = `<h1> ${data['parse']['title']} </h1> ${data['parse']['text']}`
            }).catch(err => {
                wiki_viewer.innerHTML = `<h1> 이런! </h1> ${err.message} 잠시 후 다시 시도해주세요.`
            })
        }).finally(() => {
            wiki_viewer.classList.add("active")
        })
}

function close_stic_wiki() {
    let wiki_viewer = document.getElementById("wiki_viewer")
    wiki_viewer.innerHTML = "";
    wiki_viewer.classList.remove("active");
}