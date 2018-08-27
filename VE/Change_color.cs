using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Change_color : MonoBehaviour {
    public Material[] materials;
    public Renderer rend;
    private int index;

    // Use this for initialization
    void Start () {
        rend = GetComponent<Renderer> ();
        rend.enabled = true;
    }
	
	
    void OnMouseDown()
    {
        if (materials.Length == 0)
        {
            return;
        }
        if (Input.GetButtonDown("space"))
        {
            index += 1;
            if (index == materials.Length + 1)
            {
                index = 1;
            }
            rend.sharedMaterial = materials[index - 1];
        }

  
    }

  


}
