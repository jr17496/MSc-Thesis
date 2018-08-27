using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Controler : MonoBehaviour {
	public float moveSpeed;

	// Use this for initialization
	void Start () {
		moveSpeed = 40;
	}
	
	// Update is called once per frame
	void Update () {
		transform.Translate(Input.GetAxis("Horizontal") * Time.deltaTime * moveSpeed, 0f, Input.GetAxis("Vertical") * Time.deltaTime * moveSpeed);
	}
}
