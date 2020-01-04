if [[ $1 == '--run' ]]; then
	if [[ $2 == '3_bot.py' ]]; then
		sudo python $2 &
	elif [[ $2 == '1_bot.py' ]]; then
		sudo python $2 &
	elif [[ $2 == '2_bot.py' ]]; then
		sudo python $2 &
	else
		sudo kill +3 $(pgrep python)
		sleep 2
		sudo python status_bot.py &
		sudo python 3_bot.py &
		sudo python 1_bot.py &
		sudo python 2_bot.py &
	fi
	# echo Excelent run!
elif [[ $1 == '--kill' ]]; then
	if [[ $2 == 'all' ]]; then
		sudo kill +3 $(pgrep python)
		sleep 2
		sudo python status_bot.py &
	elif [[ $2 == '3_bot.py' ]]; then
		sudo kill +3 $(pgrep python)
		sleep 2
		sudo python status_bot.py &
		sudo python 1_bot.py &
		sudo python 2_bot.py &
	elif [[ $2 == '1_bot.py' ]]; then
		sudo kill +3 $(pgrep python)
		sleep 2
		sudo python status_bot.py &
		sudo python 3_bot.py &
		sudo python 2_bot.py &
	elif [[ $2 == '2_bot.py' ]]; then
		sudo kill +3 $(pgrep python)
		sleep 2
		sudo python status_bot.py &
		sudo python 3_bot.py &
		sudo python 1_bot.py &
	fi
fi

