function ClearCache() {
    let r = confirm("Are you sure to clear local cache?\nThis is not reversible!");
    if(r == true){
        alert("Delete Complete!")
        location.replace("/polls/delete_all_local_cache/")
    }
}