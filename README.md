# bookhmsrvr
Python / Flask webapp for accessing your book collection in local network

## Usage howto
1. Clone the repository and move to project's folder
2. Either install all the [needed packages](requirements.txt) manually, or
   source project's [`setup_dev.sh`](setup_dev.sh) script
3. Make sure you have a postgres server, and you have rights to create new
   databases there
4. Fill all the needed data in [`config.ini`](config.ini) file
4. Launch the app at least once (`python3 src/app.py <secret code>`).
   It is needed to create all required tables in your database
4. Add some books with [`add_data.py`](src/add_data.py) script.

   This requires
   - [`data_config`](data_config.ini) to be filled correctly
   - postgres database to be up and running

## Contribution
Checkout [CONTRIBUTION.md](./CONTRIBUTION.md)

Feel free to
[submit an issue](https://github.com/mb6ockatf/bookhmsrvr/issues/new)
if you've found an error / have a question / has a feature idea etc.

by *@mb6ockatf*, 16.04.2023
