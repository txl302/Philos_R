import time

def run_tri(m_id, current_pos, des_pos, time_inv):
	current_time = time.time()
	des_time  = current_time + time_inv
	n = len(m_id)
	time_tmp = time.time()

	pose = current_pos

	v_top = []
	k =[]

	for i in range(n):
		v_top.append(2*(des_pos[i] - current_pos[i])/time_inv)
	for i in range(n):
		k.append(v_top[i]*2/time_inv)



	while time.time()<= des_time:
		time_slot = time.time() - time_tmp
		time_tmp = time.time()



		if time_tmp <= current_time + time_inv/2:
			speed = []
			for i in range(n):
				speed.append(k[i]*(time_tmp - current_time))
			for i in range(n):
				pose[i] += speed[i]*time_slot


		elif (time_tmp >= current_time + time_inv/2) & (time_tmp <= des_time):
			speed = []
			for i in range(n):
				speed.append(k[i]*(des_time - time_tmp))
			for i in range(n):
				pose[i] += speed[i]*time_slot

		print pose

def main():
	ids = [1, 2]
	current_pos = [30, 0]
	des_pos = [80, 80]
	time_inv = 3
	run_tri(ids, current_pos, des_pos, time_inv)
	run_tri(ids, des_pos, current_pos, time_inv)

if __name__ == '__main__':
	main()