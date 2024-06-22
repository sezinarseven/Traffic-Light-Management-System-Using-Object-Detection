using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class carScript : MonoBehaviour
{
    public float speed = 5.0f;

    private Rigidbody rb;
    gameManager gm;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
        gm = GameObject.Find("gameManager").GetComponent<gameManager>();
    }
    void Update()
    {
        transform.Translate(Vector3.forward * speed * Time.deltaTime);
        if ((transform.position.z <= -8) && (transform.position.z >= -8.2f) && (gm.red1))
        {
            speed = 0;
        }
        if (!gm.red1)
        {
            speed = 5;
        }
    }
    
    private void OnCollisionEnter(Collision collision)
    {
        if ((collision.gameObject.tag == "car") && (gm.red1))
        {
                speed = 0;
        }
        if (collision.gameObject.tag == "finisher")
        {
            Destroy(this.gameObject);
        }
    }
}
