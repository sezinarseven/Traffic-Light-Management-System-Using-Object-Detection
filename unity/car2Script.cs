using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class car2Script : MonoBehaviour
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
        if ((transform.position.x <= -5.5f) && (transform.position.x >= -5.7f) && (gm.red2))
        {
            speed = 0;
        }
        if (!gm.red2)
        {
            speed = 5;
        }
    }
    
    private void OnCollisionEnter(Collision collision)
    {
        if ((collision.gameObject.tag == "car") && (gm.red2))
        {
            speed = 0;
        }
        if (collision.gameObject.tag == "finisher")
        {
            Destroy(this.gameObject);
        }
    }
}
