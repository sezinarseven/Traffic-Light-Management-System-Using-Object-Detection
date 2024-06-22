using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class gameManager : MonoBehaviour
{
    public GameObject redLight;
    public GameObject greenLight;
    public GameObject yellowLight;
    public GameObject redLight2;
    public GameObject greenLight2;
    public GameObject yellowLight2;
    public GameObject carPrefab;
    public GameObject carPrefab2;
    public GameObject stoppingBar1;
    public GameObject stoppingBar2;
    public float spawnTime = 6.0f;
    private float timePassed = 0.0f;
    public Vector3 spawnPoint;
    public float spawnTime2 = 7.0f;
    private float timePassed2 = 0.0f;
    public Vector3 spawnPoint2;
    public Vector3 spawnPoint3;
    public Vector3 spawnPoint4;
    public bool red1;
    public bool red2;
    

    private void Start()
    {
        red1 = true;
        red2 = true;
        redLight.SetActive(true);
        redLight2.SetActive(true);
    }
    
    private void Update()
    {
        timePassed += Time.deltaTime;
        timePassed2 += Time.deltaTime;
        if (timePassed >= spawnTime)
        {
            createCar();
            timePassed = 0.0f;
        }
        if (timePassed2 >= spawnTime2)
        {
            createCar2();
            timePassed2 = 0.0f;
        }
        if (Input.GetKeyDown(KeyCode.K))
        {
            StartCoroutine(TrafficLights1());
        }
        if (Input.GetKeyDown(KeyCode.L))
        {
            StartCoroutine(TrafficLights2());
        }
    }

    void createCar()
    {
        Instantiate(carPrefab, spawnPoint, Quaternion.identity);
        Quaternion rotation = Quaternion.Euler(0, 90, 0);
        Instantiate(carPrefab2, spawnPoint3, rotation);
    }
    
    void createCar2()
    {
        Instantiate(carPrefab, spawnPoint2, Quaternion.identity);
        Quaternion rotation = Quaternion.Euler(0, 90, 0);
        Instantiate(carPrefab2, spawnPoint4, rotation);
    }


    private IEnumerator TrafficLights1()
    {
        greenLight2.SetActive(false);
        
        yellowLight2.SetActive(true);
        red2 = true;
        
        yield return new WaitForSeconds(1.5f);
        yellowLight2.SetActive(false);

        redLight2.SetActive(true);
        
        yield return new WaitForSeconds(1.5f);
        redLight.SetActive(false);
        
        yellowLight.SetActive(true);
        yield return new WaitForSeconds(1.5f);
        yellowLight.SetActive(false);
        
        greenLight.SetActive(true);
        red1 = false;
    }
    private IEnumerator TrafficLights2()
    {
        greenLight.SetActive(false);
        
        yellowLight.SetActive(true);
        yield return new WaitForSeconds(1.5f);
        yellowLight.SetActive(false);

        redLight.SetActive(true);
        red1 = true;

        yield return new WaitForSeconds(1.5f);
        redLight2.SetActive(false);
        
        yellowLight2.SetActive(true);
        yield return new WaitForSeconds(1.5f);
        yellowLight2.SetActive(false);
        
        greenLight2.SetActive(true);
        red2 = false;
    }
}
